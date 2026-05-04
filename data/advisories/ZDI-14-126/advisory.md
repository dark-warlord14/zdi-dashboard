# ZDI-14-126: Google Chrome ImageData Signedness Error Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-126
- **ZDI-CAN:** ZDI-CAN-2245
- **Date:** 2014-05-13
- **CVE:** CVE-2014-1736
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-126/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ImageData objects. In certain conditions, an attacker would be able to read and write pixel data. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2014/04/stable-channel-update_24.html 359802

## Disclosure Timeline

- 2014-04-03 - Vulnerability reported to vendor
- 2014-05-13 - Coordinated public release of advisory
