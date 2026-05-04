# ZDI-17-709: EMC Data Protection Advisor ReportQueueResource orderby SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-709
- **ZDI-CAN:** ZDI-CAN-4694
- **Date:** 2017-08-25
- **CVE:** CVE-2017-8002
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** EMC
- **Affected Products:** Data Protection Advisor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-709/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of EMC Data Protection Advisor. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be easily bypassed. The specific flaw exists within the EMC DPA Application service, which listens on TCP port 9002 by default. When parsing the orderby request parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/fulldisclosure/2017/Jul/12

## Disclosure Timeline

- 2017-04-12 - Vulnerability reported to vendor
- 2017-08-25 - Coordinated public release of advisory
