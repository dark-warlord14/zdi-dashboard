# ZDI-15-137: (Pwn2Own) Google Chrome pnacl Shared Memory Time-Of-Check/Time-Of-Use Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-137
- **ZDI-CAN:** ZDI-CAN-2833
- **Date:** 2015-04-15
- **CVE:** CVE-2015-1234
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-137/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of communication between the GPU process and the renderer processes. The issue lies in the verification of values from the renderer without copying them out of a shared memory section. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2015/04/stable-channel-update.html

## Disclosure Timeline

- 2015-03-19 - Vulnerability reported to vendor
- 2015-04-15 - Coordinated public release of advisory
