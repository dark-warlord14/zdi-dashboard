# ZDI-15-144: ManageEngine OpManager MigrateCentralData zipFileName File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-144
- **ZDI-CAN:** ZDI-CAN-2451
- **Date:** 2015-04-15
- **CVE:** CVE-2014-7866
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ManageEngine
- **Affected Products:** OpManager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-144/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ManageEngine OpManager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MigrateCentralData servlet. The issue lies in the failure to sanitize the filenames uploaded to the servlet. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://support.zoho.com/portal/manageengine/helpcenter/articles/fix-for-remote-code-execution-via-file-upload-vulnerability

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2015-04-15 - Coordinated public release of advisory
