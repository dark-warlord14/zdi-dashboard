# ZDI-10-024: Novell eDirectory SOAP Request Parsing Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-024
- **ZDI-CAN:** ZDI-CAN-440
- **Date:** 2010-03-02
- **CVE:** CVE-2010-0666
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:C
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-024/
## Vulnerability Details

This vulnerability allows remote attackers to deny services on vulnerable installations of Novell eDirectory Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NDS daemon's SOAP service. When a malformed request is made to the novell.embox.connmgr.serverinfo SOAP action, the daemon makes an illegal reference thereby resulting in a denial of service.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7005341

## Disclosure Timeline

- 2009-03-13 - Vulnerability reported to vendor
- 2010-03-02 - Coordinated public release of advisory
