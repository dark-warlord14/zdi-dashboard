# ZDI-25-898: Delta Electronics COMMGR Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-898
- **ZDI-CAN:** ZDI-CAN-25289
- **Date:** 2025-09-18
- **CVE:** CVE-2025-53418
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** COMMGR
- **Credit:** Guillaume Orlando
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-898/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics COMMGR. An attacker must first obtain the ability to compromise a PLC in order to exploit this vulnerability. The specific flaw exists within the handling of packets received from a PLC. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the application.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://filecenter.deltaww.com/news/download/doc/Delta-PCSA-2025-00014_COMMGR%20Stack-based%20Buffer%20Overflow%20and%20Code%20Injection%20Vulnerabilities.pdf

## Disclosure Timeline

- 2025-06-19 - Vulnerability reported to vendor
- 2025-09-18 - Coordinated public release of advisory
- 2025-09-18 - Advisory Updated
