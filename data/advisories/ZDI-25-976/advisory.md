# ZDI-25-976: Delta Electronics ASDA-Soft PAR File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-976
- **ZDI-CAN:** ZDI-CAN-27128
- **Date:** 2025-10-29
- **CVE:** CVE-2025-62580
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** ASDA-Soft
- **Credit:** Guillaume Orlando
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-976/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics ASDA-Soft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PAR files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-296-04

## Disclosure Timeline

- 2025-06-09 - Vulnerability reported to vendor
- 2025-10-29 - Coordinated public release of advisory
- 2025-10-29 - Advisory Updated
