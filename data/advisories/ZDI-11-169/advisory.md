# ZDI-11-169: IBM Tivoli Endpoint lcfd.exe opts Argument Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-169
- **ZDI-CAN:** ZDI-CAN-964
- **Date:** 2011-05-31
- **CVE:** CVE-2011-1220
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Endpoint
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-169/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Endpoint. Authentication is required to exploit this vulnerability, however it is trivially achieved. The specific flaw exists within the lcfd.exe process which listens by default on TCP port 9495. To reach this page remotely authentication is required. However, by abusing a built-in account an attacker can access the restricted pages. While parsing requests to one of these, the process blindly copies the contents of a POST variable to a 256 byte stack buffer. This can be leveraged by a remote attacker to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www-304.ibm.com/support/docview.wss?uid=swg21499146

## Disclosure Timeline

- 2010-11-23 - Vulnerability reported to vendor
- 2011-05-31 - Coordinated public release of advisory
