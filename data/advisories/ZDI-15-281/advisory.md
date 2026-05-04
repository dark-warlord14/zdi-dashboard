# ZDI-15-281: WebKit WebSQL ALTER TABLE Authorization Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-281
- **ZDI-CAN:** ZDI-CAN-2900
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3727
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WebKit.Org
- **Affected Products:** WebKit
- **Credit:** Peter Rutenbar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-281/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WebSQL. The issue lies in the failure to properly utilize SQLite's authorization code. An attacker can leverage this vulnerability to execute restricted SQL statements under the context of the current process.

## Additional Details

WebKit.Org has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2015-04-24 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
