# ZDI-19-019: OMRON CX-One CX-Protocol CObject Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-019
- **ZDI-CAN:** ZDI-CAN-6585
- **Date:** 2019-01-14
- **CVE:** CVE-2018-19027
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-One
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OMRON CX-One CX-Protocol. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PSW files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-010-02

## Disclosure Timeline

- 2018-07-03 - Vulnerability reported to vendor
- 2019-01-14 - Coordinated public release of advisory
