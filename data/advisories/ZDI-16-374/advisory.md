# ZDI-16-374: SolarWinds Storage Resource Monitor Profiler Server RulesMetaData addNewRule SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-374
- **ZDI-CAN:** ZDI-CAN-3398
- **Date:** 2016-06-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SolarWinds
- **Affected Products:** Storage Resource Monitor
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-374/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Storage Resource Monitor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RulesMetaData's addNewRule method which is reachable through the ScriptServlet servlet. The issue lies in the failure to sanitize user-supplied input prior to executing a SQL statement. An attacker could leverage this vulnerability to execute code under the context of the database, which defaults to SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://thwack.solarwinds.com/community/cloud-virtualization-storage_tht/storage-manager/blog/2016/06/10/srm-profiler-module-formerly-known-as-storage-manager-v623-hot-fix-1-is-available

## Disclosure Timeline

- 2016-02-16 - Vulnerability reported to vendor
- 2016-06-22 - Coordinated public release of advisory
