# ZDI-17-314: Google Chrome List Item Marker Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-314
- **ZDI-CAN:** ZDI-CAN-4429
- **Date:** 2017-05-02
- **CVE:** CVE-2017-5059
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-314/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of list item markers. It's possible to trigger a type confusion condition by manipulating a document's elements. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromereleases.googleblog.com/2017/04/stable-channel-update-for-desktop.html

## Disclosure Timeline

- 2017-01-24 - Vulnerability reported to vendor
- 2017-05-02 - Coordinated public release of advisory
