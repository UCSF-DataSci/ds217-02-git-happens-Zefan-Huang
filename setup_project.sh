#!/bin/bash 
# Create project structure

echo "Setting up project..."

mkdir -p src data output 


cat > .gitignore << 'EOF'
# Python cache files
__pycache__/
*.pyc

# Data and secrets
data/raw/*.csv
.env
*.key
EOF

cat>requirements.txt << 'EOF'
EOF


cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,85,Math
Bob,22,90,Science
Charlie,21,78,History
David,23,88,Math
Eve,20,92,Science
Frank,22,75,History
Grace,21,80,Math
Heidi,23,95,Science
Ivan,20,70,History
Judy,22,89,Math
Louis,21,84,Science
EOF

cat > src/data_analysis.py << 'EOF'
def data_analysis():
    # TODO: Here's somthing to do based on the part 3.
    pass

EOF

cat > src/data_analysis_functions.py << 'EOF'
def data_analysis_functions():
    # TODO: Here's somthing to do based on the part 3.
    pass
EOF
