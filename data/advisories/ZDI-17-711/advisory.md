# ZDI-17-711: EMC Data Protection Advisor ScheduledReportResource Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-711
- **ZDI-CAN:** ZDI-CAN-4695
- **Date:** 2017-08-25
- **CVE:** CVE-2017-8003
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** EMC
- **Affected Products:** Data Protection Advisor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-711/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of EMC Data Protection Advisor. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be easily bypassed. The specific flaw exists within the EMC DPA Application service, which listens on TCP port 9002 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose any files accessible to the SYSTEM user.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/fulldisclosure/2017/Jul/12

## Disclosure Timeline

- 2017-04-12 - Vulnerability reported to vendor
- 2017-08-25 - Coordinated public release of advisory
