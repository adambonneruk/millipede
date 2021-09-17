# millipede

Apply multiple regex "Search and Replace" (SaR) rules to a single document. Using consecutive SaR rules, lines can be transformed using several simple steps each building on top of one another. I think this keeps things simple whilst aiding debugging. Using python we can even comment each SaR rule for future reference.

## Example

Using three rules we can (1) remove vowels, (2) replace full stops, and (3) remove spaces.

### Replacement Rules

```python
regex_sar_rules = [
    [r"[aeiou]", ""], # Remove Vowels
    [r"\.", "_"], # Replace PEriod/Full Stop with Underscore
    [r" ", ""] # Remove Spaces
]
```

### Results Table (```test/foobar.txt```)

| Before | After |
| ------ | ----- |
| Forename | Frnm |
| Surname | Srnm |
| Bank Details.Account Number | BnkDtls_AccntNmbr |
| Bank Details.Sort Code | BnkDtls_SrtCd |
| Address.Street | Addrss_Strt |
| Address.Post Code | Addrss_PstCd |
| Address.Country | Addrss_Cntry |