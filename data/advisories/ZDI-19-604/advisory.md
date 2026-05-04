# ZDI-19-604: Advantech WebAccess Node viewsrv fileno Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-604
- **ZDI-CAN:** ZDI-CAN-8137
- **Date:** 2019-07-02
- **CVE:** CVE-2019-10993
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-604/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x2781 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-178-05

## Disclosure Timeline

- 2019-03-01 - Vulnerability reported to vendor
- 2019-07-02 - Coordinated public release of advisory
