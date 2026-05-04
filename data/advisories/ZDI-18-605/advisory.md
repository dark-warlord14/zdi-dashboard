# ZDI-18-605: Apple Safari InputType Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-605
- **ZDI-CAN:** ZDI-CAN-6107
- **Date:** 2018-07-10
- **CVE:** CVE-2018-4263
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Arayz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-605/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HTML access keys. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208934

## Disclosure Timeline

- 2018-04-25 - Vulnerability reported to vendor
- 2018-07-10 - Coordinated public release of advisory
- 2018-07-10 - Advisory Updated
