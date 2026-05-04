# ZDI-10-027: Skype Protocol Handler datapath Argument Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-027
- **ZDI-CAN:** ZDI-CAN-510
- **Date:** 2010-03-11
- **CVE:** N/A
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:N
- **Affected Vendors:** Skype
- **Affected Products:** Skype
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-027/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Skype. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists with how the OS web-browser passes command line arguments to Skype through the registered 'skype:' protocol handler. Insufficient sanity checking to the /datapath argument allows an attacker to construct a link that will execute Skype with arbitrary arguments. This can be abused to specify a remote configuration storage directory which can be leveraged to glean target user credentials.

## Additional Details

Skype has issued an update to correct this vulnerability. More details can be found at: http://share.skype.com/sites/garage/2010/03/10/ReleaseNotes_4.2.0.155.pdf

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2010-03-11 - Coordinated public release of advisory
