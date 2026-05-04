"""Extract review sample CSV from matrix + enum mappings."""
import csv

# Load matrix
with open(r'D:\ARD\mappings\tta-0976_x_components.csv', encoding='utf-8') as f:
    matrix = list(csv.reader(f))
matrix_header = matrix[0]
matrix_rows = matrix[1:]

# Load enum
with open(r'D:\ARD\mappings\tta-0976_enumerations_mapping.csv', encoding='utf-8') as f:
    enum = list(csv.reader(f))
enum_header = enum[0]
enum_rows = enum[1:]

# Sample selection
samples = []  # (source, id, term_name, mapping, priority, confidence_or_status, reason_for_review)

# 1. Random 20 (matrix 11 + enum 9 — pre-selected per Step 4 plan)
random_matrix_ids = ['TTA-0976-002','TTA-0976-015','TTA-0976-023','TTA-0976-102','TTA-0976-105','TTA-0976-113','TTA-0976-117','TTA-0976-204','TTA-0976-213','TTA-0976-304','TTA-0976-326']
random_enum_ids = ['TTA-0976-CV-005','TTA-0976-CV-021','TTA-0976-CV-044','TTA-0976-CV-058','TTA-0976-CV-068','TTA-0976-CV-076','TTA-0976-CV-095','TTA-0976-CV-103','TTA-0976-CV-110']

for r in matrix_rows:
    if r[0] in random_matrix_ids:
        samples.append(('matrix', r[0], r[1], r[4], r[11], r[12], 'random_sample (분포 확인)'))
for r in enum_rows:
    if r[0] in random_enum_ids:
        samples.append(('enum', r[0], r[1], r[3], r[5], '-', 'random_sample (분포 확인)'))

# 2. 발견 사항 관련 10행
discovery_matrix = {
    'TTA-0976-323': '발견#1 Coverage dual-purpose (sh:or 처리)',
    'TTA-0976-327': '발견#2 File Unit Rule 3 사례',
    'TTA-0976-009': '발견#4 SKOS Concept 4계층 (Repository Subject)',
    'TTA-0976-109': '발견#4 SKOS Concept 4계층 (Collection Subject)',
    'TTA-0976-212': '발견#4 SKOS Concept 4계층 (Dataset Subject)',
    'TTA-0976-314': '발견#4 SKOS Concept 4계층 (File Subject)',
    'TTA-0976-022': '발견#5 Boolean Activation Slot (QualityManagement)',
}
discovery_enum = {
    'TTA-0976-CV-014': '발견#4 SKOS Concept 관련 (DFG SubjectScheme)',
    'TTA-0976-CV-091': '발견#5 Boolean Slot 활성 트리거 (yes)',
    'TTA-0976-CV-055': '발견#2 Rule 3 관련 (FileSizeUnitType Byte)',
}

for r in matrix_rows:
    if r[0] in discovery_matrix:
        samples.append(('matrix', r[0], r[1], r[4], r[11], r[12], discovery_matrix[r[0]]))
for r in enum_rows:
    if r[0] in discovery_enum:
        samples.append(('enum', r[0], r[1], r[3], r[5], '-', discovery_enum[r[0]]))

# 3. low/secondary 등급 전체
existing_ids = {s[1] for s in samples}
for r in matrix_rows:
    if r[0] in existing_ids:
        continue
    if r[11] == 'secondary' or r[12] == 'medium':
        reason = f"matrix {r[11]}/{r[12]} (확신 낮음)"
        samples.append(('matrix', r[0], r[1], r[4], r[11], r[12], reason))
for r in enum_rows:
    if r[0] in existing_ids:
        continue
    if r[5] in ('secondary','none'):
        reason = f"enum {r[5]} (확신 낮음 또는 매핑 부재)"
        samples.append(('enum', r[0], r[1], r[3], r[5], '-', reason))

# Write sample CSV
with open(r'D:\ARD\mappings\tta-0976_review_sample.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['source','inventory_id','term_name','mapping','priority','confidence','reason_for_review'])
    for s in samples:
        w.writerow(s)

print(f'Total sample rows: {len(samples)}')
print()
print('By source:')
from collections import Counter
print(' ',dict(Counter(s[0] for s in samples)))
print()
print('By reason category:')
for s in samples[:10]: print(f'  {s[1]}: {s[6]}')
print(f'  ... ({len(samples)-10} more)')
