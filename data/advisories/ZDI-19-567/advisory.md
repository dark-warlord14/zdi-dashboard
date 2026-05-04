# ZDI-19-567: Panasonic Control FPWIN PRO Project File Parsing sc_app Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-567
- **ZDI-CAN:** ZDI-CAN-7852
- **Date:** 2019-06-13
- **CVE:** CVE-2019-6530
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Panasonic
- **Affected Products:** Control FPWIN Pro
- **Credit:** 9sg Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-567/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Panasonic Control FPWin Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PRO files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Panasonic has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-157-02

## Disclosure Timeline

- 2019-02-04 - Vulnerability reported to vendor
- 2019-06-13 - Coordinated public release of advisory
