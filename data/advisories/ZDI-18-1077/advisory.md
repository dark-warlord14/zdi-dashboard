# ZDI-18-1077: (Pwn2own) Samsung Galaxy S8 Shannon GPRS Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1077
- **ZDI-CAN:** ZDI-CAN-5368
- **Date:** 2018-09-21
- **CVE:** CVE-2018-14318
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S8
- **Credit:** Acez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung Galaxy S8. User interaction is required to exploit this vulnerability in that the target must have their cellular radios enabled. The specific flaw exists within the handling of IPCP headers. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the baseband processor.

## Additional Details

Patched with 2018 JAN SMR

## Disclosure Timeline

- 2017-11-01 - Vulnerability reported to vendor
- 2018-09-21 - Coordinated public release of advisory
- 2018-09-25 - Advisory Updated
