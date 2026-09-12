RendaMensal = float
score = int 0 <= 1000 com restrição

aprovado | score >= 700 and RendaMensal > 4000 and sem restricoes (bool)
reaprovar | RendaMensal >= 2500 and sem restricoes and score >= 500 or RendaMensal > 6000
recursar | else