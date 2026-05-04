# ZDI-14-293: (0Day) F5 Data Manager discoverFilerBasicInfo.jsft filerName SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-293
- **ZDI-CAN:** ZDI-CAN-2308
- **Date:** 2014-08-12
- **CVE:** CVE-2014-2949
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** F5
- **Affected Products:** Data Manager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-293/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of F5 Data Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the discoverFilerBasicInfo.jsft page. An attacker is able to inject SQL through the filerName field in this page, and use that to gain full administrator credentials for Data Manager.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/02/2014 - ZDI disclosed vulnerability to vendor 05/12/2014 - Vendor acknowledged 06/16/2014 - ZDI wrote F5 to ask for clarification about: http://support.f5.com/kb/en-us/solutions/public/15000/300/sol15310.html 06/16/2014 - Vendor wrote that they notified ZDI of closure on 06/09/2014 (this was not received) and indicated that "our publications team has determined that this release provides the appropriate level of disclosure" 06/17/2014 - ZDI acknowledged 06/18/2014 - ZDI wrote to confirm mitigation only 06/18/2014 - Vendor requested contact 06/19/2014 - ZDI replied 07/25/2014 - ZDI again wrote to confirm our understanding 08/12/2014 - ZDI published advisory -- Vendor Mitigation: To mitigate this vulnerability, you can stop the Data Manager Service when not in use. To do so, perform the following procedure: Impact of action: Performing the following procedure should not have a negative impact on your system. Log in as admin to Data Manager Web Application. In the left navigation tree, click Tasks. Ensure that all tasks are completed (or canceled) before proceeding. Close the Data Manager Web Application. From the Programs menu, open the Data Manager Control Panel. Click the Main tab. In the Service Status section, click the Stop button. When necessary, you can restart the Data Manager Service by clicking the Start button. http://support.f5.com/kb/en-us/solutions/public/15000/300/sol15310.html

## Disclosure Timeline

- 2014-05-02 - Vulnerability reported to vendor
- 2014-08-12 - Coordinated public release of advisory
