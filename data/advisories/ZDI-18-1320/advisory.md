# ZDI-18-1320: Apple macOS WindowServer XRegisterForKey Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1320
- **ZDI-CAN:** ZDI-CAN-5813
- **Date:** 2018-10-30
- **CVE:** CVE-2018-4193
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1320/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the WindowServer process. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges under the context of the WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208849

## Disclosure Timeline

- 2018-02-20 - Vulnerability reported to vendor
- 2018-10-30 - Coordinated public release of advisory
- 2018-10-30 - Advisory Updated
