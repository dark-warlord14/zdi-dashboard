# ZDI-11-127: CA Total Defense Suite UNCWS Web Service getDBConfigSettings Credential Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-127
- **ZDI-CAN:** ZDI-CAN-1037
- **Date:** 2011-04-13
- **CVE:** CVE-2011-1655
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** CA
- **Affected Products:** Total Defense Suite
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-127/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CA Total Defense Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists within the management.asmx module of the Management Web Service. This process responds to SOAP 1.2 requests on port 34444 for HTTP and port 34443 for HTTPS. Due to a flaw in the implementation of the getDBConfigSettings method, it is possible for an unauthenticated user to obtain the server's database credentials, which are transmitted via plaintext. Given the database credentials, it is trivial for a remote user to authenticate to the server and execute arbitrary code under the context of the database administrator.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID={CD065CEC-AFE2-4D9D-8E0B-BE7F6E345866}

## Disclosure Timeline

- 2010-12-16 - Vulnerability reported to vendor
- 2011-04-13 - Coordinated public release of advisory
