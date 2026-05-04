# ZDI-16-224: Google Chrome libANGLE glGetUniformfv Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-224
- **ZDI-CAN:** ZDI-CAN-3623
- **Date:** 2016-04-08
- **CVE:** CVE-2016-1649
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-224/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the libANGLE library. The issue lies in the failure to safely copy data from buffers of disparate types. An attacker can leverage this vulnerability to execute code within the context of the GPU process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2016/03/stable-channel-update_24.html

## Disclosure Timeline

- 2016-03-16 - Vulnerability reported to vendor
- 2016-04-08 - Coordinated public release of advisory
