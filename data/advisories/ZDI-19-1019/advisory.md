# ZDI-19-1019: Advantech DiagAnywhere FILE_CREATE Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1019
- **ZDI-CAN:** ZDI-CAN-9485
- **Date:** 2019-12-13
- **CVE:** CVE-2019-18257
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** DiagAnywhere
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech DiagAnywhere. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of FILE_CREATE messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the server process.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-346-01

## Disclosure Timeline

- 2019-11-20 - Vulnerability reported to vendor
- 2019-12-13 - Coordinated public release of advisory
