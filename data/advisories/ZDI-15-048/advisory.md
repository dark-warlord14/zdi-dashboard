# ZDI-15-048: Dell ScriptLogic Asset Manager GetClientPackage SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-048
- **ZDI-CAN:** ZDI-CAN-2334
- **Date:** 2015-02-20
- **CVE:** CVE-2015-1605
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Dell
- **Affected Products:** Asset Manager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Dell ScriptLogic Asset Manager, also known as Quest Workspace Asset Manager. Authentication is not required to exploit this vulnerability. To exploit this security flaw, an attacker would make a specially crafted web request to a handler named GetClientPackage.aspx that is installed as part of this product. An attacker can leverage this vulnerability to execute code under the context of NETWORK SERVICE.

## Additional Details

Dell has issued an update to correct this vulnerability. More details can be found at: https://support.software.dell.com/asset-manager/9.5

## Disclosure Timeline

- 2014-05-27 - Vulnerability reported to vendor
- 2015-02-20 - Coordinated public release of advisory
