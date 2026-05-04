# ZDI-18-1330: Advantech WebAccess Client bwswfcfg Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1330
- **ZDI-CAN:** ZDI-CAN-7166
- **Date:** 2018-10-31
- **CVE:** CVE-2018-17910
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1330/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess Client. Authentication is not required to exploit this vulnerability. The specific flaw exists within bwswfcfg.exe, which is accessed through the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-298-02

## Disclosure Timeline

- 2018-08-22 - Vulnerability reported to vendor
- 2018-10-31 - Coordinated public release of advisory
