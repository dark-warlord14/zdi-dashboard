# ZDI-25-888: (0Day) Digilent DASYLab DSB File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-888
- **ZDI-CAN:** ZDI-CAN-26613
- **Date:** 2025-11-20
- **CVE:** CVE-2025-57775
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Digilent
- **Affected Products:** DASYLab
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-888/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Digilent DASYLab. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DSB files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/memory-corruption-vulnerabilities-in-digilent-dasylab.html

## Disclosure Timeline

- 2025-06-09 - Vulnerability reported to vendor
- 2025-11-20 - Coordinated public release of advisory
- 2025-11-20 - Advisory Updated
