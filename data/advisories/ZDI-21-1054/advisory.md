# ZDI-21-1054: Advantech WebAccess BwFLApp Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1054
- **ZDI-CAN:** ZDI-CAN-12967
- **Date:** 2021-09-03
- **CVE:** CVE-2021-38408
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1054/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of IOCTL 0x2711, which can be used to invoke BwFLApp.exe. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-245-03

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-09-03 - Coordinated public release of advisory
