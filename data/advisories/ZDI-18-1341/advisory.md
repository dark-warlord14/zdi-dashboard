# ZDI-18-1341: Apple macOS nsurlstoraged Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1341
- **ZDI-CAN:** ZDI-CAN-6137
- **Date:** 2018-11-05
- **CVE:** CVE-2018-4126
- **CVSS:** 1.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Bruno Keith (@bkth_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1341/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of cookie data. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209139

## Disclosure Timeline

- 2018-05-09 - Vulnerability reported to vendor
- 2018-11-05 - Coordinated public release of advisory
- 2018-11-05 - Advisory Updated
