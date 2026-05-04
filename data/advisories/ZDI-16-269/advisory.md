# ZDI-16-269: SolarWinds Storage Resource Monitor Profiler Module ScriptServlet SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-269
- **ZDI-CAN:** ZDI-CAN-3397
- **Date:** 2016-04-28
- **CVE:** CVE-2016-4350
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SolarWinds
- **Affected Products:** Storage Resource Monitor Profiler Module
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-269/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Storage Resource Monitor Profiler Module. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of the ScriptServlet servlet in the SolarWinds Storage Manager Web Services web server. The state parameter is vulnerable to SQL injection when it begins with "updatescript". This allows an attacker to run arbitrary code as SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://www.solarwinds.com/documentation/storage/storagemanager/docs/ReleaseNotes/releaseNotes.htm

## Disclosure Timeline

- 2015-11-25 - Vulnerability reported to vendor
- 2016-04-28 - Coordinated public release of advisory
