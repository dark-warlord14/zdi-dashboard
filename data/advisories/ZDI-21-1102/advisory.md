# ZDI-21-1102: Schneider Electric EcoStruxure Control Expert Classic STU and STA File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1102
- **ZDI-CAN:** ZDI-CAN-13461
- **Date:** 2021-09-20
- **CVE:** CVE-2021-22797
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Control Expert Classic
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1102/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric EcoStruxure Control Expert Classic. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of STU and STA files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-259-02

## Disclosure Timeline

- 2021-05-05 - Vulnerability reported to vendor
- 2021-09-20 - Coordinated public release of advisory
