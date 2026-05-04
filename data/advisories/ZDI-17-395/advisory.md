# ZDI-17-395: Trend Micro Maximum Security tmusa Kernel Driver Untrusted Pointer Dereference Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-395
- **ZDI-CAN:** ZDI-CAN-4191
- **Date:** 2017-06-13
- **CVE:** N/A
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-395/
## Vulnerability Details

This vulnerability allows local attackers to deny service on vulnerable installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of IOCTL 0x00222813 in tmusa.sys. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this to deny service to the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117509

## Disclosure Timeline

- 2017-02-02 - Vulnerability reported to vendor
- 2017-06-13 - Coordinated public release of advisory
