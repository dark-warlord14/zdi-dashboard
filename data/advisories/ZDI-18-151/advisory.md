# ZDI-18-151: (Pwn2Own) Apple Safari UIProcess Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-151
- **ZDI-CAN:** ZDI-CAN-5345
- **Date:** 2018-02-07
- **CVE:** CVE-2017-7172
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-151/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Apple Safari. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of ResourceRequest objects. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code under the context of the user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208334

## Disclosure Timeline

- 2017-11-02 - Vulnerability reported to vendor
- 2018-02-07 - Coordinated public release of advisory
- 2018-02-07 - Advisory Updated
