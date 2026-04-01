param(
    [Parameter(Mandatory = $true)]
    [string]$Branch
)

$repo = "C:\Users\ervin\PeopleMap"

git -C $repo push -u origin $Branch
