# ZDI-10-112: Novell Access Manager Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-112
- **ZDI-CAN:** ZDI-CAN-635
- **Date:** 2010-06-21
- **CVE:** CVE-2010-0284
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Access Manager
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-112/
## Vulnerability Details

This vulnerability allows remote attackers to upload arbitrary files on vulnerable installations of Novell Access Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PortalModuleInstallManager component of the Novell Management Console which exists within the servlet located within nps.jar. Due to a failure to sanitize '../' directory traversal modifiers from a parameter an attacker can specify any filename to upload arbitrary contents into. Successful exploitation can result in code execution under the context of the service.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7006255&sliceId=1&docTypeID=DT_TID_1_1&dialogID=149517296&stateId=0%200%20149513677,

## Disclosure Timeline

- 2009-12-10 - Vulnerability reported to vendor
- 2010-06-21 - Coordinated public release of advisory
