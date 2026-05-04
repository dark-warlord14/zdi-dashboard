# ZDI-20-834: Advantech iView NetworkServlet Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-834
- **ZDI-CAN:** ZDI-CAN-10646
- **Date:** 2020-07-16
- **CVE:** CVE-2020-14503
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-834/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetworkServlet servlet. The issue results from the lack of proper validation of user-supplied data prior to further processing. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-196-33

## Disclosure Timeline

- 2020-04-01 - Vulnerability reported to vendor
- 2020-07-16 - Coordinated public release of advisory
