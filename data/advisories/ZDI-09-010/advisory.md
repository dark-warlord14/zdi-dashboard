# ZDI-09-010: Novell Netware Groupwise GWIA RCPT Command Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-010
- **ZDI-CAN:** ZDI-CAN-384
- **Date:** 2009-02-02
- **CVE:** CVE-2009-0410
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Nick DeBaggis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-010/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Netware Groupwise SMTP daemon. Authentication is not required to exploit this vulnerability. The specific flaw exists during the parsing of malformed RCPT verb arguments to the SMTP daemon. When an overly long e-mail address is received an off-by-one condition is triggered which minimally will cause a denial of service and can result in arbitrary code execution.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=GjZRRdqCFW0

## Disclosure Timeline

- 2008-08-26 - Vulnerability reported to vendor
- 2009-02-02 - Coordinated public release of advisory
