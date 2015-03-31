#!/bin/env perl

# pac file is from url: https://raw.githubusercontent.com/clowwindy/gfwlist2pac/master/test/proxy.pac
open(FS, "<", "gfwlist.pac") or die $!;
{
    local $/=undef;
    $content = <FS>;
    close(FS);
}

if ($content =~ /var\s+domains\s*=\s*\{(.*?)\}/isg)
{
   @lines = split(/\n/, $1);
}

my @domains;
foreach $line (@lines)
{
    $line =~ s/\s+//g;
    @items = split(/:/, $line);
    if ($items[0] =~ /^\s*$/) { next };
    push @domains, $items[0].",";
}

@domains = sort(@domains);
$domain = join("\n        ", @domains);
#print $domain;
#print "\n"; 

open(FS, "<", "myproxy.pac") or die $!;
{
    local $/=undef;
    $content = <FS>;
    close(FS);
}

$content =~ s/<domains-from-gfwlist>/$domain/isg;

print $content

