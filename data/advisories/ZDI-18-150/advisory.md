# ZDI-18-150: (Pwn2Own) Apple Safari FTL JIT Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-150
- **ZDI-CAN:** ZDI-CAN-5344
- **Date:** 2018-02-07
- **CVE:** CVE-2017-7160
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-150/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arguments to JavaScript functions. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208334

## Disclosure Timeline

- 2017-11-02 - Vulnerability reported to vendor
- 2018-02-07 - Coordinated public release of advisory
- 2018-02-07 - Advisory Updated
