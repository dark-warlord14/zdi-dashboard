# ZDI-18-1321: (Pwn2Own) Apple Safari CreateThis Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1321
- **ZDI-CAN:** ZDI-CAN-5819
- **Date:** 2018-10-30
- **CVE:** CVE-2018-4233
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Samuel Gross (saelo)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1321/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JIT. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208848

## Disclosure Timeline

- 2018-04-07 - Vulnerability reported to vendor
- 2018-10-30 - Coordinated public release of advisory
- 2018-10-30 - Advisory Updated
