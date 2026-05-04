# ZDI-10-190: Novell iManager getMultiPartParameters Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-190
- **ZDI-CAN:** ZDI-CAN-772
- **Date:** 2010-10-01
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iManager
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-190/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell iManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the nps.jar web application exposed via the Tomcat server running by default on TCP ports 8080 and 8443. The com.novell.nps.serviceProviders.PortalModuleInstallManager servlet exposes a function called getMultiPartParameters which parses POST variables from a multipart form request. The getEntry function that the above uses can be made to write an arbitrary file to disk. An attacker can abuse this to place a malicious JSP document in a web-accessible location. By uploading a malicious script, this can be leveraged to execute remote code under the context of the Tomcat process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7006515&sliceId=2

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-10-01 - Coordinated public release of advisory
