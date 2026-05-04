# ZDI-15-276: Apple QuickTime Plugin Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-276
- **ZDI-CAN:** ZDI-CAN-2574
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3665
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** WanderingGlitch of HP's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-276/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the properties for the QuickTime browser plugin. By manipulating a QuickTime object's properties an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2014-10-22 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
