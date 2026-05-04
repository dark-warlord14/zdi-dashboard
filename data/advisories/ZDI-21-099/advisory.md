# ZDI-21-099: Fuji Electric V-Server Lite VPR File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-099
- **ZDI-CAN:** ZDI-CAN-11669
- **Date:** 2021-01-29
- **CVE:** CVE-2021-22641
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** V-Server Lite
- **Credit:** khangkito - Tran Van Khang of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-099/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric V-Server Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VPR files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-026-01

## Disclosure Timeline

- 2020-09-02 - Vulnerability reported to vendor
- 2021-01-29 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
