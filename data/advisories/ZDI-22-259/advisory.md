# ZDI-22-259: Advantech WebAccess IOCTL 0x1138B Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-259
- **ZDI-CAN:** ZDI-CAN-12966
- **Date:** 2022-02-02
- **CVE:** CVE-2021-38389
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-259/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of IOCTL 0x1138B. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-21-285-02

## Disclosure Timeline

- 2021-06-14 - Vulnerability reported to vendor
- 2022-02-02 - Coordinated public release of advisory
