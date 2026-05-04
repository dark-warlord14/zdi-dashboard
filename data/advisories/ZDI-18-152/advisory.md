# ZDI-18-152: (Pwn2Own) Apple Safari HTMLButtonElement Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-152
- **ZDI-CAN:** ZDI-CAN-5352
- **Date:** 2018-02-07
- **CVE:** CVE-2017-7165
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** 360 Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-152/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HTMLButtonElement objects. By performing actions in JavaScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208334

## Disclosure Timeline

- 2017-11-02 - Vulnerability reported to vendor
- 2018-02-07 - Coordinated public release of advisory
- 2018-02-07 - Advisory Updated
