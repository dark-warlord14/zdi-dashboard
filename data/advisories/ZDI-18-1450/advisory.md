# ZDI-18-1450: (Pwn2Own) Samsung Galaxy S8 Shannon Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1450
- **ZDI-CAN:** ZDI-CAN-5785
- **Date:** 2019-03-04
- **CVE:** CVE-2018-14319
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S8
- **Credit:** acez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1450/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung Galaxy S8. User interaction is required to exploit this vulnerability in that the target must answer a phone call. The specific flaw exists within the handling of Status Information Elements. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the baseband processor.

## Additional Details

https://security.samsungmobile.com/securityUpdate.smsb -> 2018 -> August -> SVE-2018-11828: Buffer Overflow in Exynos Chipset Devices with Security Patch Level (SPL) of August 1st, 2018 or later will include the patch for this issue.

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2019-03-04 - Coordinated public release of advisory
- 2019-03-05 - Advisory Updated
