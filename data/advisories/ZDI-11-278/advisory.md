# ZDI-11-278: Novell Cloud Manager Insufficient Framework User Validation Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-278
- **ZDI-CAN:** ZDI-CAN-1154
- **Date:** 2011-09-02
- **CVE:** CVE-2011-2654
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-278/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Cloud Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within how the application implements an RPC method. Due to incompletely initializing an object, the application will store a partially initialized session. This partially initialized session will allow one to make privileged RPC calls to the server. This can lead to code execution under the context of the service.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=NSONlV5PqMo~

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-09-02 - Coordinated public release of advisory
