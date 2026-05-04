# ZDI-18-1065: (0Day) Quest KACE Systems Management run_report Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1065
- **ZDI-CAN:** ZDI-CAN-6111
- **Date:** 2018-09-18
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Quest
- **Affected Products:** KACE Systems Management
- **Credit:** Kapil Khot (SlidingWindow)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Quest KACE Systems Management. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the ID and FMT parameters provided to the run_report page. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to remotely execute code under the context of root.

## Additional Details

Quest has issued an update to correct this vulnerability. More details can be found at: https://support.quest.com/kb/261499/zero-day-initiative-zdi-report-update There is a hotfix available for those customers running 9.0.270 that can be applied to their appliance if they don't want to wait for the upcoming 9.1.x release. This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/20/18 - ZDI reported the vulnerabilities to the vendor 09/12/18 - ZDI notified the vendor of the intention to disclose the report as 0-day on 9/18/18 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2018-04-20 - Vulnerability reported to vendor
- 2018-09-18 - Coordinated public release of advisory
- 2018-10-01 - Advisory Updated
