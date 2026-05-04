# ZDI-17-827: Dell EMC VNX Monitoring and Reporting Scheduler Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-827
- **ZDI-CAN:** ZDI-CAN-4754
- **Date:** 2017-09-26
- **CVE:** CVE-2017-8007
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Dell EMC
- **Affected Products:** VNX Monitoring and Reporting
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-827/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Dell EMC VNX Monitoring and Reporting. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within Scheduler.class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Dell EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/fulldisclosure/2017/Sep/51

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-09-26 - Coordinated public release of advisory
