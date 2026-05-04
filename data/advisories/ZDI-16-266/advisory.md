# ZDI-16-266: SolarWinds Storage Resource Monitor Profiler Module XiotechMonitorServlet SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-266
- **ZDI-CAN:** ZDI-CAN-3377
- **Date:** 2016-04-28
- **CVE:** CVE-2016-4350
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SolarWinds
- **Affected Products:** Storage Resource Monitor Profiler Module
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-266/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Storage Resource Monitor Profiler Module. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of the XiotechMonitorServlet servlet in the SolarWinds Storage Manager Web Services web server. If the state parameter is set to the value listDepartments, then the parameters sortField and sortDirection are vulnerable to SQL injection. This allows an attacker to run arbitrary code as SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/storage/storagemanager/docs/ReleaseNotes/releaseNotes.htm

## Disclosure Timeline

- 2015-11-20 - Vulnerability reported to vendor
- 2016-04-28 - Coordinated public release of advisory
