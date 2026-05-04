# ZDI-21-098: Fuji Electric V-Server Lite VPR File Parsing Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-098
- **ZDI-CAN:** ZDI-CAN-11668
- **Date:** 2021-01-29
- **CVE:** CVE-2021-22639
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** V-Server Lite
- **Credit:** khangkito - Tran Van Khang of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-098/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric V-Server Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VPR files. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-026-01

## Disclosure Timeline

- 2020-09-02 - Vulnerability reported to vendor
- 2021-01-29 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
