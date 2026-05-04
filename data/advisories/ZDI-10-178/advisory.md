# ZDI-10-178: Novell PlateSpin Orchestrate Graph Rendering Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-178
- **ZDI-CAN:** ZDI-CAN-680
- **Date:** 2010-09-15
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-178/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Platespin Orchestrate. Authentication is not required to exploit this vulnerability. The specific flaw exists within how the application utilizes a bundled component for rendering graphs. The application will pass user-supplied arguments to this component without proper sanitization. An attacker can abuse this to specify arbitrary arguments to this tool. Successful exploitation will lead to code execution in the context of the graph component application.

## Additional Details

http://www.novell.com/support/viewContent.do?externalId=7007075

## Disclosure Timeline

- 2010-02-02 - Vulnerability reported to vendor
- 2010-09-15 - Coordinated public release of advisory
